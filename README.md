# UI-automation


python+appium+unittest自动化框架结构
	config
		appium配置信息
		driver_config.py
	common
		封装基本操作：元素定位、输入、截图、滑动、获取toast内容等
		base_method.py
	data
		元素信息：xpath、id等
		element.yml
	page
		封装页面：登录页，播放页等，包括元素定位和操作
		login.py
		albumplay.py
		...
	testcase
		测试用例：以封装的页面为维度区分
		test_login.py
		test_albumplay.py
	run.py
		测试用例执行，生成测试报告
	report
		存储测试报告：xxxx-xx-xx xx:xx:xx.html
