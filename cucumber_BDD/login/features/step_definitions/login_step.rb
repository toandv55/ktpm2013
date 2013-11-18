require 'watir-webdriver'
require 'rspec'

browser = Watir::Browser.new :firefox

Given(/^I am on "(.*?)"$/) do |home|
    browser.goto home
end

When(/^I click on the button Đăng nhập at home page$/) do
    browser.link(:id => 'login').click
end

When(/^I fill "(.*?)" in textbox Tên đăng nhập$/) do |username|
    browser.text_field(:id => 'id_username').set(username)
end

When(/^I fill "(.*?)" in textbox Mật khẩu$/) do |pass|
    browser.text_field(:id => 'id_password').set(pass)
end

When(/^I click on the button Đăng nhập at login page$/) do
    browser.input(:id => 'login').click
end

Then(/^I see a page with the text "(.*?)"$/) do |school_name|
    browser.text.should include(school_name)    
end



