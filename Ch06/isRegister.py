import configparser
import os

config = None
FILE_PATH = 'myconfig.ini'

def writeConfig(section: str, option: str, data: str):
    try:
        iniConfig = configparser.ConfigParser()
        s = str(data, encoding='utf-8')
        if not os.path.exists(FILE_PATH):
            iniConfig.add_section(section)
            iniConfig.set(section, option, s)
            iniConfig.write(open(FILE_PATH, "w"))
        else:
            if section not in iniConfig.sections():
                iniConfig.add_section(section)
            iniConfig.read(FILE_PATH, encoding="utf-8")
            iniConfig.set(section, option, s)
            iniConfig.write(open(FILE_PATH, "w"))
        print(f"Write temp config file (section: {section}, option: {option}, value: {data})")
    except Exception as e:
        print(e)
    return None

def main():
    global config
    database = {'database': {'host': '127.0.0.1',
                             'user': 'root',
                             'passwd': '123',
                             'port': 3306,
                             'db': 'pet'}}
    # 初始化配置对象
    config = configparser.ConfigParser()

    # 新建myconfig.ini配置文件
    config.read(FILE_PATH)
    for section in database:
        for option in database[section]:
            if 'database' not in config.sections():
                config.add_section(section)
            config.set(section, option, str(database[section][option]))
            config.write(open(FILE_PATH, 'w'))

def delete():
        # 判断database节下是否有encoding键名
    if config.has_option('database', 'encoding'):
        # 删除配置文件中的encoding键
        config.remove_option('database', 'encoding')
        config.write(open(FILE_PATH, 'w'))
        print("已删除配置文件中的encoding键")
    else:
        # 添加encoding键到配置文件中
        config.set('database', 'encoding', 'utf-8')
        config.write(open(FILE_PATH, 'w'))
    print("已添加encoding键到配置文件中")

def database():
    # 判断是否有database节
    if 'database' in config.sections():
        # 显示database节下所有option的键值对和键名
        print("database节下所有键值对和键名：")
        for key, value in config.items('database'):
            print(f"键名：{key}，键值：{value}")
        
        # 获取database节下port键对应的值
        port = config.get('database', 'port')
        print(f"database节下port键对应的值：{port}")
    else:
        # 添加database节到配置文件中
        config.add_section('database')
        config.set('database', 'port', '3306')
        config.write(open(FILE_PATH, 'w'))
        print("已添加database节到配置文件中")

def display():
    # 显示所有节 sections
    print("所有节 sections: ", config.sections())



if __name__ == '__main__':
    main()
    display()
    database()
    delete()

