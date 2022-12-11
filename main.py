def func_that_prints_function_name_and_argument_values(func, arg=None):
    if arg is None:
        arg = []

    func_name = func.__name__.replace('_', ' ').title()
    str_arg = ' '
    for i in range(len(arg)):
        str_arg = str_arg + arg[i] + ' '

    return func_name + str_arg


def open_browser(browser_name):
    name_func_and_arguments = func_that_prints_function_name_and_argument_values(open_browser, [browser_name])
    return name_func_and_arguments


print(open_browser(browser_name="Chrome"))


def go_to_companyname_homepage(page_url):
    name_func_and_arguments = func_that_prints_function_name_and_argument_values(go_to_companyname_homepage,
                                                                                 [page_url])
    return name_func_and_arguments


print(go_to_companyname_homepage(page_url='https://otus.ru/nest/post/622/'))


def find_registration_button_on_login_page(page_url, button_text):
    name_func_and_arguments = func_that_prints_function_name_and_argument_values(find_registration_button_on_login_page,
                                                                                 [page_url, button_text])
    return name_func_and_arguments


print(find_registration_button_on_login_page(page_url='https://python-scripts.com/range', button_text='Ок'))