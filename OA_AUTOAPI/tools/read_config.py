import configparser

class ReadConfig():
    def read_config(self,file_name,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf[section][option]


    def read_config_section(self,file_name,section):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        # print(cf.items(section))
        return dict(cf.items(section))

if __name__ == '__main__':
    import os
    from conf.project_path import test_config_path

    db_data = ReadConfig().read_config_section(os.path.join(test_config_path, "case.config"), "DB")
    print(db_data)
