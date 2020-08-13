import configparser

class ReadConfig():
    def read_config(self,fileName,section,option):
        cf = configparser.ConfigParser()
        cf.read(fileName,encoding="utf-8-sig")
        return cf[section][option]

    def read_config_as_section(self,fileName,section):
        cf = configparser.ConfigParser()
        cf.read(fileName ,encoding="utf-8-sig")
        return dict(cf.items(section))

if __name__ == '__main__':
    from conf.project_path import test_config_path
    s = ReadConfig().read_config(test_config_path, "project", "url")
    d = ReadConfig().read_config_as_section(test_config_path,"DB")
    print(s,d)