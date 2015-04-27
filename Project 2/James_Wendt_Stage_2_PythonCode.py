def generate_takeaway_html(takeaway_title, takeaway_description):
    html_text_1 = '''
<div class="takeaway">
    <div class="takeaway-title">
        ''' + takeaway_title
    html_text_2 = '''    
    </div>
    <div class="takeaway-description">
        ''' + takeaway_description 
    html_text_3 = '''
    </div>
</div> '''   
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

    def get_title(takeaway):
    start_location = takeaway.find('TITLE:')
    end_location =  takeaway.find('DESCRIPTION:')
    title = takeaway[start_location+7:end_location-1]
    return title

    def get_description(takeaway):
    start_location = takeaway.find('DESCRIPTION:')
    description = takeaway[start_location+13: ]
    return description

    def get_takeaway_by_number(text, takeaway_number):
    counter = 0
    while counter < takeaway_number:
        counter = counter + 1
        next_takeaway_starts = text.find('TITLE:')
        next_takeaway_ends = text.find('TITLE:', next_takeaway_starts + 1)
        if next_takeaway_ends >= 0:
            takeaway = text[next_takeaway_starts:next_takeaway_ends]
        else: 
            next_takeaway_ends = len(text)
            takeaway = text[next_takeaway_starts:]
        text = text[next_takeaway_ends:]
    return takeaway

    def generate_all_html_text(text):
    current_takeaway_number = 1
    takeaway = get_takeaway_by_number(text, current_takeaway_number)
    all_html = ''
    while takeaway != '':
        title = get_title(takeaway)
        description = get_description(takeaway)
        takeaway_html = generate_takeaway_html(title, description)
        all_html = all_html + takeaway_html
        current_takeaway_number = current_takeaway_number + 1
        takeaway = get_takeaway_by_number(text, current_takeaway_number)
    return all_html    