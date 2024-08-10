from django import template
import math

register = template.Library()

#function to calculate read time
@register.filter
def calculateReadTime(story_content):
    #remove nbsp; and convert to spaces in string
    story_content = story_content.replace("&nbsp;", " ")

    #count number of words in the string
    word_count = len(story_content.split())
    # #200 words per minute
    reading_speed = word_count/200
    
    return math.ceil(reading_speed)

register.filter('calculateReadTime', calculateReadTime)