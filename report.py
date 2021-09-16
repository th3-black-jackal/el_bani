import datetime
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from jinja2.exceptions import TemplateNotFound
import pdfkit
import pandas as pd


class Report(object):
    def __init__(self, root_path):
        self.root_path = root_path
        self.initialize_paths()
        self.template_name = None
        self.stylesheet = None


    def initialize_paths(self):
        self.raw_templates_path = self.root_path + "/templates/raw_templates/"
        self.rendered_templates_path = self.root_path + "/templates/rendered_templates/"
        self.reports_path = self.root_path + "/reports/"
        self.stylesheets_path = self.root_path + "/static/css/"

    def set_stylesheet(self, stylesheet):
        self.stylesheet = self.stylesheets_path + stylesheet

    def get_stylesheet(self):
        return self.stylesheet

    def get_date(self, date, date_format=None):
        """
        Get a date string and return date in the requested format, default is yyyy-mm-dd
        """
        if not date_format:
            date_format = "%Y-%m-%d"
        return date.strftime(date_format)

    def read_items(self, csv_file, cols):
        items = pd.read_csv(csv_file, usecols=cols)
        self.items = items
    
    """
    This function must be overriden in order to function
    """

    def render_report(self):
        env = Environment(loader=FileSystemLoader(self.raw_templates_path), autoescape=select_autoescape())
        """
        Check if the user assigned the template name
        """
        template = env.get_template(self.template_name)

    def generate_report(self, report_name):
        pdfkit.from_file(self.rendered_templates_path + self.template_name, self.reports_path + report_name)

    def save_rendered_page(self, rendered_page):
        with open(self.rendered_templates_path + self.template_name, "w") as output_file:
            output_file.write(rendered_page)    


