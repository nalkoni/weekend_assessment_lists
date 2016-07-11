# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def total_cost_w_tax(tax_rate, state, cost_amount):
    """
     Returns the total cost of item including tax and the state

    """
    state.upper()
    default_tax_rate = 0.05
    if state == 'CA':
        total_cost = (cost_amount * .07) + cost_amount
    elif tax_rate != 0.07 or tax_rate != 0.05:
        total_cost = (cost_amount * tax_rate) + cost_amount
    else:
        total_cost = (cost_amount * default_tax_rate) + cost_amount
    return total_cost, state.upper()
#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".


def is_berry(fruit):
    """ Returns a boolean if the fruit is a "strawberry", "cherry", or
     "blackberry

    """
    if fruit == 'strawberry' or fruit == 'cherry' or fruit == 'blackberry':
        is_berry = True
    else:
        is_berry = False
    return is_berry

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit):
    """
    Returns shipping_cost based on inputed fruit

    I've been trying to make this work... I don't know why it is not
    calling the function. I can write it to do it without calling function

    """
    if is_berry(fruit):
        shipping_cost = 0
    else:
        shipping_cost = 5
    return shipping_cost


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
def is_hometown(town):
    """
    Returns whether town inputed is True or False

    """
    if town == 'orlando':
        is_hometown = True
    else:
        is_hometown = False
    return is_hometown
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


def full_name(first_name, last_name):
    """
    Returns concatenation of first and last name

    """
    return first_name + " " + last_name


#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def hometown_greeting(hometown, first_name, last_name):
    if is_hometown(hometown):
        greeting = "Hi %s, we're from the same place!" % full_name(first_name, last_name)
    else:
        greeting = "Hi %s, where are you from?" % full_name(first_name, last_name)
    return greeting

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################