# -*- coding: utf-8 -*-
from tkinter import scrolledtext

import requests
from bs4 import BeautifulSoup
import tkinter as tk


def get_weather_info(url, choose_all=False):
    try:
        # 发起请求并设置超时时间为两秒
        response = requests.get(url, timeout=2)

        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取.day div的文本内容
        day_divs = soup.find_all('div', class_='day')
        day_text_list = [div.get_text() for div in day_divs]

        # 输出今天的城市和天气信息
        if choose_all:
            result = [",".join([item.strip() for item in day_text.split("\n") if item.strip()]) for day_text in
                      day_text_list]
            return result
        else:
            for day_text in day_text_list:
                day_info = [item.strip() for item in day_text.split("\n") if item.strip()]
                return day_info
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None


def show_weather_info(city):
    if not city:
        text_area.delete('1.0', tk.END)  # 清空文本框内容
        text_area.insert(tk.END, "请先输入要查询的城市名")  # 插入错误信息
        return

    print(f"{city}")
    try:
        url = 'https://weather.cma.cn/web/weather/' + href_list[text_list.index(city)]
        weather_info = get_weather_info(url)

        if weather_info:
            print("城市：", city)
            print(weather_info)

        if weather_info:
            text_area.delete('1.0', tk.END)  # 清空文本框内容
            text_area.insert(tk.END, f"城市：{city}\n")  # 插入新的天气信息
            text_area.insert(tk.END, weather_info)  # 插入新的天气信息

    except ValueError:
        text_area.delete('1.0', tk.END)  # 清空文本框内容
        text_area.insert(tk.END, f"很抱歉，暂时查找不到城市\"{city}\"的天气状况")  # 插入错误信息
        raise ValueError(f"很抱歉，暂时查找不到城市\"{city}\"的天气状况")


# 城市名和链接可以在https://weather.cma.cn/中添加更多城市，名字和链接对应的
href_list = ['58367', '51463', '52889', '54511', '58238', '58606', '58321', '53463', '50953', '53772', '59287', '56294',
             '55591', '56778', '58457', '57494', '54342', '54823', '59758', '59493', '53698', '58847', '52866', '57036',
             '57816', '57083', '57516', '53614', '54161', '57679', '54517', '45005', '45011', '58968', '59431',
             '062721', '003772', '068816', '061641', 'G05021', '065563', '063260', '064950', 'G05020', '063980',
             '061832', '065472', '067665', '067341', '064500', 'G05019', '061442', 'G05025', '063125', '063450',
             '063740', '065125', '064700', 'G05024', '067775', '060390', 'G05018', '063894', '064390', '008589',
             '063705', 'G05017', '065387', '064387', '060135', '067083', '060715', '040103', '062010', '062366',
             '064810', 'G05009', '061291', '047108', '044292', '048698', '097390', '048647', '048074', '048991',
             '048820', '048940', '096315', '041571', '043466', '041923', '044454', '043555', '041217', '040582',
             '017130', '041170', '041256', '040100', '040438', '041150', '040754', '040650', '040948', '037864',
             '037545', '037788', '035188', '038353', '038836', '038457', '048455', '096741', '098425', '041404',
             'G05010', '027612', '011035', '016716', '012375', '013274', '011520', '015614', '011816', '013615',
             '014240', '014654', '013462', '026038', '026730', '014014', '012843', '013586', '015420', '026422',
             '033345', '026850', '033815', 'G05005', '008535', 'G05011', '093439', '094035', 'G05007', 'G05022',
             'G05004', 'G05014', 'G05013', 'G05003', 'G05012', '085574', 'G05023', '006240', '086580', '080415',
             'G05016', 'G84071', '084628', '078762', '078806', 'G05015', 'G05006', '078970', '078862', 'G05026',
             'G05008', 'G05002', '078224', 'G05001', '047662', '072405', '006180', '094926', '076680', '040080',
             '\ufeff001492', '040270', '061052', '083377', '007149', '087582', '006451', '047058', '042299', '076405',
             '002464', '042182', '010385', '065344', '071628', '064650', '065503', '016242', '040183', '067001',
             '002974', '061990', '064210', '038880', '008221', 'map', '58367', '51463', '52889', '54511', '58238',
             '58606', '58321', '53463', '50953', '53772', '59287', '56294', '55591', '56778', '58457', '57494', '54342',
             '54823', '59758', '59493', '53698', '58847', '52866', '57036', '57816', '57083', '57516', '53614', '54161',
             '57679', '54517', '45005', '45011', '58968', '59431', '54511', '53463', '53772', '53698', '54517', '54401',
             '54610', '54602', '54534', '54515', '54423', '54616', '54449', '54702', '53798', '53892', '53868', '53588',
             '53764', '53487', '53778', '53674', '53771', '53976', '53578', '53959', '53882', '53782', '53878', '53543',
             '53513', '50838', '53512', '53068', '53446', '54113', '50527', '54218', '54135', '54102', '52576', '53602',
             '53480', '50953', '54342', '54161', '54172', '54157', '54292', '50946', '54273', '54266', '54291', '50936',
             '54371', '54260', '54363', '54377', '50971', '50774', '50873', '50442', '50973', '50884', '50850', '50842',
             '50136', '54094', '50741', '50853', '54096', '50978', '50775', '50468', '50745', '54497', '54662', '54353',
             '54324', '54346', '54563', '54471', '54453', '54347', '54249', '54337', '54237', '54339', '54338', '58367',
             '58238', '58606', '58321', '58457', '54823', '58847', '54736', '54938', '54774', '54714', '54945', '58024',
             '54827', '54915', '54830', '54734', '54843', '54765', '54806', '54828', '54906', '54857', '58102', '58311',
             '58424', '58433', '58122', '58326', '58427', '58116', '58224', '58236', '58334', '58221', '58429', '58203',
             '58336', '58531', '58251', '58259', '58131', '58343', '58027', '58245', '58354', '58145', '58246', '57494',
             '57083', '57679', '57051', '57297', '57178', '57195', '58005', '53898', '57171', '57091', '53986', '57073',
             '53978', '57186', '58207', '54900', '53982', '57089', '57290', '53990', '57485', '57256', '57590', '57483',
             '57482', '57370', '57461', '57447', '57279', '57475', '57362', '57476', '57377', '57278', '57496', '57381',
             '57399', '57498', '58407', '57978', '57776', '57649', '57763', '57584', '57662', '57558', '57749', '59287',
             '59758', '59493', '59289', '59485', '59471', '59087', '59288', '57996', '59298', '59315', '59117',
             '591170', '59316', '59501', '59293', '59280', '59658', '59312', '59488', '59664', '592780', '59659',
             '59663', '59082', '59480', '59313', '59278', '59473', '59951', '59948', '59838', '59842', '59940', '59945',
             '59845', '59851', '59854', '59856', '59843', '59849', '59855', '59848', '59954', '59644', '59425', '59242',
             '59046', '51463', '52889', '52866', '57036', '53614', '57048', '57143', '57245', '57016', '53845', '53646',
             '57127', '57045', '53947', '52984', '52532', '57006', '52995', '53915', '53829', '52652', '52679', '56096',
             '52896', '52533', '52856', '52754', '52875', '52737', '52818', '56065', '52853', '56029', '56043', '51431',
             '51243', '51238', '51573', '51828', '52203', '51709', '51133', '51379', '51656', '51368', '51357', '51356',
             '51628', '56294', '55591', '56778', '57816', '57516', '57348', '57522', '57536', '56386', '57503', '57411',
             '56492', '56385', '57313', '57206', '57415', '56198', '56666', '57508', '57602', '56146', '56391', '56196',
             '56396', '56571', '56298', '57328', '57405', '56171', '56287', '56951', '56651', '56748', '56751', '56964',
             '56994', '56586', '56959', '56768', '56844', '56875', '56838', '56975', '56533', '56543', '57907', '57825',
             '57806', '45005', '45011', '58968', '59562', '59158', '59358', '59354', '58964', '59162', '59152', '58965',
             '59362', '59554', '047108', '044292', '048698', '097390', '048647', '048097', '048074', '048991', '048820',
             '048900', '048940', '096315', '041571', '041780', '041530', '043466', '041923', '044454', '043555',
             '041217', '040582', '017060', '017130', '041170', '041256', '040100', '040438', '040477', '041024',
             '041030', '041150', '040800', '040754', '040848', '040745', '040650', '040948', '040990', '037864',
             '037545', '037788', '035188', '038353', '038836', '038457', '048455', '097230', '096741', '003772',
             'G05010', '027459', '031561', '028440', '031735', '026063', '029634', '031960', '027612', '011035',
             '016716', '012375', '013274', '011520', '015614', '011816', '013615', '013334', '014240', '014654',
             '013462', '026038', '026730', '014014', '012843', '013586', '015420', '026422', '033345', '026850',
             '033815', 'G05005', '008535', '016061', 'G05011', '062315', '006180', '\ufeff001492', '008181', '007149',
             '006451', '002464', '006700', '003334', '010385', '010147', '010637', '062721', '068816', '068263',
             '068361', '061641', 'G05021', '065563', '065578', '063260', '064950', 'G05020', '063980', '061832',
             '065472', '067665', '067341', '064500', 'G05019', '061442', 'G05025', '063125', '063450', '063740',
             '065201', '065125', '064700', 'G05024', '067775', '060390', 'G05018', '063894', '064390', '008589',
             '063705', 'G05017', '065387', '064387', '060135', '060230', '067083', '060715', '040103', '062010',
             '062405', '062366', '064810', 'G05009', '061291', '078762', '078806', 'G05015', 'G05006', '078970',
             '078862', 'G05026', 'G05008', 'G05002', '060155', '078224', 'G05001', '072494', '072219', '072243',
             '072405', '071877', '083780', '071123', '071879', '076680', '091182', '071624', '072205', '072386',
             '072509', '072295', '071628', '071892', '071843', '072503', '072530', '071627', '072793', '072259',
             '072202', '071714', '085574', 'G05023', '006240', '085283', '086580', '080415', 'G05016', 'G84071',
             '084628', '083377', '087582', '076405', '080222', '016080', '083755', '007650', '093780', '093110',
             '093439', '094035', 'G05007', 'G05022', 'G05004', 'G05014', 'G05013', 'G05003', 'G05012', '094926',
             '094866', '094578', '094767', '094610', '094672']
text_list = ['上海', '乌鲁木齐', '兰州', '北京', '南京', '南昌', '合肥', '呼和浩特', '哈尔滨', '太原', '广州', '成都',
             '拉萨', '昆明', '杭州', '武汉', '沈阳', '济南', '海口', '深圳', '石家庄', '福州', '西宁', '西安', '贵阳',
             '郑州', '重庆', '银川', '长春', '长沙', '天津', '香港', '澳门', '台北', '南宁', '喀土穆', '伦敦', '开普敦',
             '达喀尔', '弗里敦', '亚穆苏克罗', '摩加迪沙', '雅温得', '朱巴', '维多利亚', '科纳克里', '阿克拉', '卢萨卡',
             '马普托', '利伯维尔', '温得和克', '努瓦克肖特', '罗安达', '吉布提市', '亚的斯亚贝巴', '内罗毕', '阿布贾',
             '恩贾梅纳', '布拉柴维尔', '哈拉雷', '阿尔及尔', '多多马', '达累斯萨拉姆', '布琼布拉', '普拉亚', '坎帕拉',
             '班珠尔', '洛美', '基加利', '拉巴特', '塔那那利佛', '突尼斯市', '的黎波里', '的黎波里', '开罗', '马拉博',
             '蒙罗维亚', '巴马科', '首尔', '乌兰巴托', '新加坡市', '帝力', '吉隆坡', '内比都', '金边', '河内', '万象',
             '斯里巴加湾市', '伊斯兰堡', '科伦坡', '达卡', '加德满都', '马累', '阿布扎比', '科威特城', '安卡拉', '多哈',
             '马斯喀特', '贝鲁特', '利雅得', '麦纳麦', '德黑兰', '巴格达', '喀布尔', '巴库', '第比利斯', '埃里温',
             '阿斯塔纳', '比什凯克', '杜尚别', '塔什干', '曼谷', '雅加达', '马尼拉', '萨那', '尼科西亚', '莫斯科',
             '维也纳', '雅典', '华沙', '贝尔格莱德', '布拉格', '索非亚', '布拉迪斯拉发', '地拉那', '萨格勒布',
             '萨拉热窝', '波德戈里察', '塔林', '维尔纽斯', '卢布尔雅那', '布达佩斯', '斯科普里', '布加勒斯特', '里加',
             '基辅', '明斯克', '基希讷乌', '瓦莱塔', '里斯本', '卢森堡', '惠灵顿', '莫尔斯比港', '阿皮亚', '阿洛菲',
             '苏瓦', '帕利基尔', '阿瓦鲁阿', '努库阿洛法', '维拉港', '圣地亚哥', '乔治敦', '阿姆斯特丹', '蒙得维的亚',
             '加拉加斯', '帕拉马里博', '基多', '利马', '圣何塞', '巴拿马城', '圣萨尔瓦多', '圣多明各', '西班牙港',
             '圣约翰', '罗索', '圣乔治', '布里奇顿', '哈瓦那', '金斯敦', '东京', '华盛顿', '哥本哈根', '堪培拉',
             '墨西哥城', '大马士革', '奥斯陆', '安曼', '尼亚美', '巴西利亚', '巴黎', '布宜诺斯艾利斯', '布鲁塞尔',
             '平壤', '廷布', '拉巴斯', '斯德哥尔摩', '新德里', '柏林', '波多诺伏', '渥太华', '班吉', '瓦加杜古', '罗马',
             '耶路撒冷', '莫罗尼', '赫尔辛基', '路易港', '金沙萨', '阿什哈巴德', '马德里', '城市预报', '上海',
             '乌鲁木齐', '兰州', '北京', '南京', '南昌', '合肥', '呼和浩特', '哈尔滨', '太原', '广州', '成都', '拉萨',
             '昆明', '杭州', '武汉', '沈阳', '济南', '海口', '深圳', '石家庄', '福州', '西宁', '西安', '贵阳', '郑州',
             '重庆', '银川', '长春', '长沙', '天津', '香港', '澳门', '台北', '南宁', '北京', '呼和浩特', '太原',
             '石家庄', '天津', '张家口', '任丘', '保定', '唐山', '廊坊', '承德', '沧州', '秦皇岛', '衡水', '邢台',
             '邯郸', '临汾', '五台山', '吕梁', '大同', '平遥', '忻州', '文水', '晋城', '朔州', '运城', '长治', '阳泉',
             '黎城', '东胜', '临河', '乌兰浩特', '乌海', '二连浩特', '包头', '巴林右旗', '海拉尔', '赤峰', '通辽',
             '锡林浩特', '阿拉善右旗', '阿拉善左旗', '集宁', '哈尔滨', '沈阳', '长春', '吉林', '四平', '延吉', '松原',
             '桦甸', '梅河口', '珲春', '白城', '白山', '辽源', '通化', '集安', '七台河', '伊春', '佳木斯', '加格达奇',
             '勃利', '双鸭山', '大庆', '杜蒙', '漠河', '牡丹江', '甘南', '绥化', '绥芬河', '鸡西', '鹤岗', '黑河',
             '齐齐哈尔', '丹东', '大连', '新宾', '朝阳', '本溪', '瓦房店', '营口', '葫芦岛', '辽阳', '铁岭', '锦州',
             '阜新', '鞍山', '盘山', '上海', '南京', '南昌', '合肥', '杭州', '济南', '福州', '东营', '临沂', '威海',
             '德州', '日照', '枣庄', '泰安', '济宁', '淄博', '滨州', '潍坊', '烟台', '聊城', '莱芜', '菏泽', '青岛',
             '亳州', '六安', '安庆', '宣城', '宿州', '巢湖', '池州', '淮北', '淮南', '滁州', '芜湖', '蚌埠', '铜陵',
             '阜阳', '马鞍山', '黄山市', '东台', '南通', '宿迁', '常州', '徐州', '扬州', '无锡', '楚州', '泰州', '武汉',
             '郑州', '长沙', '三门峡', '信阳市', '南阳市', '周口', '商丘', '安阳市', '平顶山', '开封市', '新乡市',
             '洛阳市', '济源', '漯河市', '潢川', '濮阳', '焦作市', '许昌', '驻马店市', '鹤壁', '仙桃', '十堰', '咸宁',
             '天门', '孝感', '宜城', '宜昌', '恩施', '枣阳', '潜江', '神农架', '荆州', '荆门', '襄阳', '鄂州', '随州',
             '麻城', '黄冈', '黄石', '临武', '南岳', '吉首', '娄底', '岳阳', '常德', '张家界', '怀化', '广州', '海口',
             '深圳', '东莞', '中山', '云浮', '佛冈', '佛山', '南雄', '惠州', '揭阳', '梅县', '梅州', '汕头', '汕尾',
             '河源', '清远', '湛江', '潮州', '珠海', '电白', '肇庆', '茂名', '阳江', '韶关', '顺德', '饶平', '高要',
             '鹤山', '万宁', '三亚', '东方', '临高', '乐东', '保亭', '儋州', '定安', '屯昌', '文昌', '澄迈', '琼中',
             '琼海', '白沙', '陵水', '北海', '崇左', '来宾', '柳州', '乌鲁木齐', '兰州', '西宁', '西安', '银川', '咸阳',
             '商洛', '安康', '宝鸡', '延安', '榆林', '汉中', '渭南', '铜川', '临夏', '嘉峪关', '天水', '安定', '崆峒',
             '庆城', '张掖', '武威', '武都', '白银', '酒泉', '共和', '刚察', '平安', '德令哈', '格尔木', '河南', '海晏',
             '玉树', '玛沁', '伊宁市', '克拉玛依', '博乐', '吐鲁番', '和田', '哈密', '喀什', '塔城', '奇台', '库尔勒',
             '昌吉', '沙湾', '石河子', '阿克苏', '成都', '拉萨', '昆明', '贵阳', '重庆', '奉节', '涪陵', '黔江', '乐山',
             '内江', '南充', '宜宾', '峨眉山', '巴中', '广元', '广安', '德阳', '攀枝花', '泸县', '泸州', '甘孜', '眉山',
             '绵阳', '自贡', '西昌', '资阳', '达州', '遂宁', '阿坝', '雅安', '临沧', '丽江', '保山', '大理', '思茅',
             '文山', '昭通', '景洪', '楚雄', '潞西', '玉溪', '瑞丽', '红河', '贡山', '香格里拉', '兴义', '凯里', '安顺',
             '香港', '澳门', '台北', '台东', '台中', '台南', '嘉义', '基隆', '宜兰', '新竹', '桃园', '花莲', '高雄',
             '首尔', '乌兰巴托', '新加坡市', '帝力', '吉隆坡', '仰光', '内比都', '金边', '河内', '胡志明市', '万象',
             '斯里巴加湾市', '伊斯兰堡', '卡拉奇', '白沙瓦', '科伦坡', '达卡', '加德满都', '马累', '阿布扎比',
             '科威特城', '伊斯坦布尔', '安卡拉', '多哈', '马斯喀特', '贝鲁特', '利雅得', '吉达', '吉达', '麦加',
             '麦纳麦', '伊斯法罕', '德黑兰', '设拉子', '马什哈德', '巴格达', '喀布尔', '坎大哈', '巴库', '第比利斯',
             '埃里温', '阿斯塔纳', '比什凯克', '杜尚别', '塔什干', '曼谷', '巴里岛', '雅加达', '伦敦', '尼科西亚',
             '下诺夫哥罗德', '共青城', '叶卡捷琳堡', '哈巴罗夫斯克', '圣彼得堡', '新西伯利亚', '符拉迪沃斯托克',
             '莫斯科', '维也纳', '雅典', '华沙', '贝尔格莱德', '布拉格', '索非亚', '布拉迪斯拉发', '地拉那', '斯普利特',
             '萨格勒布', '萨拉热窝', '波德戈里察', '塔林', '维尔纽斯', '卢布尔雅那', '布达佩斯', '斯科普里',
             '布加勒斯特', '里加', '基辅', '明斯克', '基希讷乌', '瓦莱塔', '里斯本', '都灵', '卢森堡', '亚历山大',
             '哥本哈根', '奥斯陆', '巴塞罗那', '巴黎', '布鲁塞尔', '斯德哥尔摩', '日内瓦', '曼彻斯特', '柏林', '汉堡',
             '法兰克福', '喀土穆', '开普敦', '比勒陀利亚', '约翰内斯堡', '达喀尔', '弗里敦', '亚穆苏克罗', '阿比让',
             '摩加迪沙', '雅温得', '朱巴', '维多利亚', '科纳克里', '阿克拉', '卢萨卡', '马普托', '利伯维尔', '温得和克',
             '努瓦克肖特', '罗安达', '吉布提市', '亚的斯亚贝巴', '内罗毕', '拉各斯', '阿布贾', '恩贾梅纳', '布拉柴维尔',
             '哈拉雷', '阿尔及尔', '多多马', '达累斯萨拉姆', '布琼布拉', '普拉亚', '坎帕拉', '班珠尔', '洛美', '基加利',
             '拉巴特', '马拉喀什', '塔那那利佛', '突尼斯市', '的黎波里', '的黎波里', '卢克索', '开罗', '马拉博',
             '蒙罗维亚', '巴马科', '圣何塞', '巴拿马城', '圣萨尔瓦多', '圣多明各', '西班牙港', '圣约翰', '罗索',
             '圣乔治', '布里奇顿', '卡萨布兰卡', '哈瓦那', '金斯敦', '三藩市', '亚特兰大', '休斯敦', '华盛顿',
             '卡尔加里', '圣保罗', '埃德蒙顿', '埃德蒙顿', '墨西哥城', '夏威夷', '多伦多', '奥兰多', '拉斯维加斯',
             '波士顿', '洛杉矶', '渥太华', '温哥华', '温尼泊', '纽约', '芝加哥', '蒙特利尔', '西雅图', '达拉斯',
             '迈阿密', '魁北克', '圣地亚哥', '乔治敦', '阿姆斯特丹', '苏克雷', '蒙得维的亚', '加拉加斯', '帕拉马里博',
             '基多', '利马', '巴西利亚', '布宜诺斯艾利斯', '拉巴斯', '波哥大', '米兰', '里约热内卢', '马塞',
             '克赖斯特彻奇', '奥克兰', '惠灵顿', '莫尔斯比港', '阿皮亚', '阿洛菲', '苏瓦', '帕利基尔', '阿瓦鲁阿',
             '努库阿洛法', '维拉港', '堪培拉', '墨尔本', '布里斯班', '悉尼', '珀斯', '阿德来德']

root = tk.Tk()  # 创建主窗口
root.title("Weather Information")  # 设置窗口标题
root.geometry("600x320")  # 设置窗口大小（宽x高）
root.resizable(False, False)  # 禁止调整窗口大小

text_area = scrolledtext.ScrolledText(root, height=10)  # 创建滚动文本框，用于显示天气信息
text_area.pack(fill=tk.BOTH, expand=True)  # 添加滚动文本框到主窗口，并自动调整大小以适应窗口大小变化

# 创建关键词标签和输入框
keyword_label = tk.Label(root, text="城市名:")
keyword_label.pack(pady=10)
keyword_entry = tk.Entry(root)
keyword_entry.pack(pady=10)

# 创建按钮并设置事件处理程序
button1 = tk.Button(root, text="天气查询", font=("Arial", 12),
                    command=lambda: show_weather_info(keyword_entry.get()))
button1.pack(side=tk.TOP, padx=10)

print("欢迎使用 Memory Weather！")
print("作者: @Memory")
print("""  
 *  
 (  `  
 )\))(    (    )       (   (  
((_)()\  ))\  (     (  )(  )\ )  
(_()((_)/((_) )\  ' )\(()\(()/(  
|  \/  (_)) _((_)) ((_)((_))(_))  
| |\/| / -_) '  \() _ \ '_| || |  
|_|  |_\___|_|_|_|\___/_|  \_, |  
                           |__/  
""")
print("----------------------------------------------------------------")
print("输入城市名，即可极速查询该城市的实时天气状况！")
print("----------------------------------------------------------------")
print("")

root.mainloop()  # 启动主窗口的消息循环，显示窗口并等待用户操作
