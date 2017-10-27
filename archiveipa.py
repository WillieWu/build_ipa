import os
import time
import plistlib

# plist文件参数说明
# http://www.matrixprojects.net/p/xcodebuild-export-options-plist/
# method: (String) The method of distribution, which can be set as any of the following:
# app-store
# enterprise
# ad-hoc
# development
# teamID: (String) The development program team identifier.
# uploadSymbols: (Boolean) Option to include symbols in the generated ipa file.
# uploadBitcode: (Boolean) Option to include Bitcode.

# 项目路径
project_path = '/Users/wuhongbin/Desktop/yudao2Temp1'
# 项目名称
project_name = 'YuDao.xcodeproj'
# ipa文件夹
IPA_dir = '/Users/wuhongbin/Desktop'

yudao_target_name = 'YuDao'
yudao_adhoc_fileName = 'XC iOS Ad Hoc: com.weiwei.yudao'
yudao_adhoc_UUID = '6f527957-8597-442c-802c-70e30f02d589'
yudao_teamID = '26N4VZYSFU'

hongyan_target_name = 'hongyan'
hongyan_adhoc_fileName = 'hy_adhoc_new_device'
hongyan_adhoc_UUID = '473b760a-3e59-426a-a0fb-14341f1fc526'
hongyan_teamID = 'HDL3K2T9R8'

miliao_target_name = 'miliao'
miliao_adhoc_fileName = 'miliao_adhoc'
miliao_adhoc_UUID = '3c6b14d6-84d3-48fc-a213-ff567d5c5897'
miliao_teamID = '4DPS4FJPL9'

def archive_IPA(set_target_name, set_provisioning_profile_UUID, teamID):

	print('\n', set_target_name, '\n', set_provisioning_profile_UUID, '\n', teamID)

	# 获取当前工作目录路径
	file_dic = os.getcwd()
	# 创建plist文件路径
	plist_path = file_dic + '/exportResult.plist'

	print('plist文件路径 ' + plist_path)

	# 参数说明在文件顶部
	dic = {
		'teamID': teamID,
		'method': 'ad-hoc',
		'uploadSymbols': True,
	}
	# 创建IPA plist文件
	plistlib.writePlist(dic, plist_path)

	print('------------------------build clean project')
	# clean 项目
	os.system('cd %s;xcodebuild clean' % project_path)

	print('------------------------build release start')

	# os.system('xcodebuild -list')
	dir_name = set_target_name + '-' + time.strftime('%Y-%m-%d--%H-%M-%S', time.localtime())

	# 创建存放IPA的文件夹
	os.system('cd %s;mkdir %s' % (IPA_dir, dir_name))

	archive_path = IPA_dir + '/' + dir_name + '/' + set_target_name + '.xcarchive'

	ipa_path = IPA_dir + '/' + dir_name + '/' + set_target_name + '_adHoc.ipa'

	print('IPA_dir: ' + IPA_dir)
	print('archive_path: ' + archive_path)
	print('ipa_path: ' + ipa_path)

	os.system('cd %s;xcodebuild archive -project %s -scheme %s -configuration Release -sdk iphoneos -archivePath %s PROVISIONING_PROFILE="%s"' % (project_path, project_name,set_target_name, archive_path, set_provisioning_profile_UUID))

	print('-------------------------export IPA')

	os.system('xcodebuild -exportArchive -archivePath %s -exportPath %s -exportOptionsPlist %s' % (archive_path, ipa_path, plist_path))

def main():

	# archive_IPA('YuDao', yudao_adhoc_UUID)

	# archive_IPA('hongyan', hongyan_adhoc_UUID)
	
	archive_IPA( miliao_target_name, miliao_adhoc_UUID, miliao_teamID)

main()
