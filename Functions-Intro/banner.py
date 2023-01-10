def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a centered sting with `**` either side

    :param text: Text that will appear inside the banner
        (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the lef and right edges
    :param screen_width: The width of the banner
        (including the 4 spaces for the ** either side).
    :raises ValueError: if string is larger than specified width.
    """
    if len(text) > screen_width - 4:
        raise ValueError('string {0} is larger than specified width {1}'
                         .format(text, screen_width))

    if text == '*':
        print('*' * screen_width)
    else:
        output_string = '**{0}**'.format(text.center(screen_width - 4))
        print(output_string)


banner_text("*",  60)
banner_text("Always look on the bright side of life...",  60)
banner_text("If life seems jolly rotten,",  60)
banner_text("There's something you've forgotten!",  60)
banner_text("And that's to laugh and smile and dance and sing,",  60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,",  60)
banner_text("Don't be silly chumps,",  60)
banner_text("Just purse your lips and whistle - that's the thing!",  60)
banner_text("And... always look on the bright side of life...",  60)
banner_text("*",  60)
