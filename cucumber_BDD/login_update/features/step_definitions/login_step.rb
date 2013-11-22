Given(/^I am on truongnha.com$/) do
    visit('/')
	#page.save_screenshot('1.png')
end

When(/^I click on the button Đăng nhập at home page$/) do
    click_link('login')
	#page.save_screenshot('2.png')
end

When(/^I fill "(.*?)" in textbox Tên đăng nhập$/) do |username|
    fill_in('id_username', :with => username)
	#page.save_screenshot('3.png')
end

When(/^I fill "(.*?)" in textbox Mật khẩu$/) do |pass|
	fill_in('id_password', :with => pass)
	#page.save_screenshot('4.png')
end

When(/^I click on the button Đăng nhập at login page$/) do
	click_button('login')
	#page.save_screenshot('5.png')
end

Then(/^I see a page with the text "(.*?)"$/) do |logout|
    page.should have_css('#logout')
	page.should have_content(logout)
	#page.save_screenshot('6.png')
end

