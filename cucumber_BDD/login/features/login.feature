Feature: Test function login of site truongnha.com
    Scenario: Login
        Given I am on "truongnha.com"
        When I click on the button Đăng nhập at home page
            And I fill "toandv" in textbox Tên đăng nhập
            And I fill "phindpeft904" in textbox Mật khẩu
            And I click on the button Đăng nhập at login page
        Then I see the a page with the text "Team_08"  

