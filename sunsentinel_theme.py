def sunsentinel_theme(): 
    black = '#000000'
    greydk = '#333333'
    greymed = '#999999'
    grey = '#cccccc'
    greylt = '#f1f1f1'
    white = '#fff'
    red = '#d80000'
    brightred = '#ff0000'
    sunrust = '#761113'
    palepink = '#ffc9bb'
    sky = '#4492e0'
    cloud = '#9dd1f6'
    navy = '#024584'

    return {
        "width": 450,
        "height": 300,
        "config": {
            "title": {
                "fontSize": 18,
                "anchor": "start", # equivalent of left-aligned
                "color": sunrust
            },
            "axisX": {
                "domain": True,
                "domainColor": greydk,
                "domainWidth": 1,
                "grid": True,
                "gridColor": grey,
                "gridWidth": 0.5,
                "labelFontSize": 12,
                "labelColor": greydk,
                "labelAngle": 0, 
                "tickColor": greydk,
                "tickSize": 5,
                "titleFontSize": 12,
            },
            "axisY": {
                "domain": True,
                "domainColor": greydk,
                "grid": True,
                "gridColor": grey,
                "gridWidth": 0.5,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "ticks": True,
                "titleFontSize": 12,
            },
            "header": {
                "labelFontSize": 16,
                "titleFontSize": 16
            },
            "range": {
                "category": [sunrust, red, palepink, grey, greydk, black],
                "diverging": [red, palepink, grey, cloud, sky],
            },
            "legend": {
                "labelFontSize": 12,
                "symbolSize": 100, # default,
                "titleFontSize": 12,
            },
            ### MARKS CONFIGURATIONS ###
            "area": {
               "fill": sunrust,
            },
            "circle": {
               "fill": sunrust,
               "size": 40
            },
            "line": {
               "color": sunrust,
               "stroke": sunrust,
               "strokeWidth": 3,
            },
            "trail": {
               "color": sunrust,
               "stroke": sunrust,
               "strokeWidth": 0,
               "size": 1,
            },
            "path": {
               "stroke": sunrust,
               "strokeWidth": 0.5,
            },
            "point": {
               "color": sunrust,
               "size": 40
            },
            "text": {
               "color": sunrust,
               "fontSize": 11,
               "align": "right",
               "size": 14,
            }, 
            "bar": {
                "size": 10,
                "binSpacing": 1,
                "continuousBandSize": 10,
#                 "discreteBandSize": 10,
                "fill": sunrust,
                "stroke": False,
            },
            "tick": {
                "color": sunrust
            }
        }   
    }

import altair as alt
alt.themes.register("sunsentinel_theme", sunsentinel_theme)
alt.themes.enable("sunsentinel_theme")