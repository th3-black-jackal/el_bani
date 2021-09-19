import os, sys
from pathlib import Path


class App(object):
        def __init__(self, app_name):
            self.ROOT_PATH = "./" + app_name + "/"
            os.mkdir(self.ROOT_PATH)
        
        def create_dirs(self):
            app_dirs = {'forms': '', 'static': ['images', 'css'], 'src': ['delegates'], 'templates': ['rendered_templates', 'raw_templates'], 
                    'tests':'', 'reports':''}
            
            """
            Creating the directories
            """
            for sub_dir in app_dirs:
                key_path = self.ROOT_PATH + sub_dir
                print("Creating directory: ", sub_dir)
                os.mkdir(key_path)
                """
                prop stands for properties
                """
                for prop_path in app_dirs[sub_dir]:
                    new_dir_path = key_path + "/" + prop_path
                    print("Creating directory: ", prop_path)
                    os.mkdir(new_dir_path)
        
        def create_files(self):
            app_files = ['models.py', 'controllers.py', '__init__.py']
            """
            Create empty files, it's not the best practice, and maybe I will visit Django code to see how it's done
            """
            for new_file in app_files:
                with open(os.path.join(self.ROOT_PATH, new_file), 'w') as empty_fiel:
                    pass

        def start_app(self):
            self.create_dirs()
            self.create_files()

"""
Check if the user passed the application name and if not prompt the user to enter one
"""

def get_app_name(argv):
    app_name = ""
    program_name, *arguments = argv
    if not arguments:
        app_name = input("Please provide the app name: ")
    else:
        app_name = arguments[0]
    return app_name

if __name__ == "__main__":
    app_name = get_app_name(sys.argv)
    new_app = App(app_name)
    new_app.start_app()

