from flask import Flask
app = Flask(__name__)
@app.route('/home')
def html_page():
    return'''<html><h1>Hello , we are here for you Noor's Website!!!!.</h1>
     <h2>This page contains photo gallery containing three types of photos: food, pets, </h2>
     <a href ="/food1">go to the photo food1</a>
     <a href ="/food3">go to the photo food3</a>
     <a href ="/space1">go to the photo space1</a>
     <a href ="/pet2">go to the photo pet2</a>
     </html>'''

@app.route('/pet1')
def pet1():
    html_content = '''
    <html>
    <head><title>pet Photo 1</title></head>
    <body>
        <h1>pet Photo 1</h1>
        <img src="http://t0.gstatic.com/licensed-image?q=tbn:ANd9GcTZCSmCzmIPm0up8wmW566cK5w3sSTUChT5UnaU3VnFxrHwoRNSnks0xUBmj2r2oeJk">
        <a href="/home">Go back to home</a>
        <a href="/pet3">Go to the next pet photo</a>
    </body>
    </html>
    '''
    return html_content

@app.route('/pet2')
def pet2():
    html_content = '''
    <html>
    <head><title>pet Photo 2</title></head>
    <body>
        <h1>pet Photo 2</h1>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW7zpG7Q2QGK9YGchMgfbXycRtDimjSCjk8w&s">
        <a href="/home">Go back to home</a>
        <a href="/pet1">Go to the previous pet photo</a>
        <a href="/pet3">Go to the next pet photo</a>
    </body>
    </html>
    '''
    return html_content


@app.route('/pet3')
def pet3():
    html_content = '''
    <html>
    <head><title>pet Photo 3</title></head>
    <body>
        <h1>pet Photo 3</h1>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW7zpG7Q2QGK9YGchMgfbXycRtDimjSCjk8w&s">
        <a href="/pet2">Go to the next pet photo</a>
    </body>
    </html>
    '''
    return html_content


@app.route('/food1')
def food1():
    return '''
        <html>
        <head><title>food1 Photo 1</title></head>
        <body>
            <h1>food Photo 1</h1>
            <p>Here's nice food1 photo!</p>
            <img src="https://www.google.com/search?sca_esv=b81c0bacdd322bb3&sca_upv=1&sxsrf=ADLYWIIZMEBWL9xUnft77HWffr2pqcHhKw:1721139780123&q=cat&udm=2&fbs=AEQNm0CiFqa26y-564csno-VFX61wSFIUOqZH6FfNsFME4Rt5im8FgLSUJUQPB6K-AcLWXPBMtWyUdqHE7fUHwcVTZ1ZSBataA6ecI7jc3BHBikUwORLDttRWyus5l2FUmGCyfD2_4ok54A8PpN57J7M9JQGmIfUTfW7HXpbBXhUZHBAfy0LoUWlNTI5GjSkj9wCvsOcilQ-iurWdCCRrCzSzfse4Tdq0w66lYReXrvmwVTpmKwQrIHc158_39ASPoNLfdKuL3mS&sa=X&ved=2ahUKEwjOzc-p4auHAxVh1QIHHcaYDaAQtKgLegQIExAB&biw=1846&bih=948&dpr=1#vhid=OvShVGTM0NYuuM&vssid=mosaic" width="400px">
            <p><a href="/home">Back to the main entrance</a></p>
            <p><a href="/food2">Next food photo</a></p>
        </body>
        </html>
    '''
@app.route('/food2')
def food2():
    return '''
        <html>
        <head><title>food Photo 2</title></head>
        <body>
            <h1>food Photo 2</h1>
            <p>Here's nice food photo!</p>
            <img src="https://www.google.com/search?q=duck&sca_esv=b81c0bacdd322bb3&sca_upv=1&udm=2&biw=1846&bih=948&sxsrf=ADLYWILIIXXPW-5KySw1hjHVI3iF5jwdFg%3A1721139784896&ei=SIKWZvu8Nviwi-gP9_2-uAQ&ved=0ahUKEwj7gPOr4auHAxV42AIHHfe-D0cQ4dUDCBA&uact=5&oq=duck&gs_lp=Egxnd3Mtd2l6LXNlcnAiBGR1Y2syChAAGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyBRAAGIAEMgUQABiABDIKEAAYgAQYQxiKBTIFEAAYgAQyChAAGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigVIkBlQgA5Y8hZwA3gAkAEAmAGoAqABjQaqAQUwLjMuMbgBA8gBAPgBAZgCB6AC6AbCAgQQIxgnmAMAiAYBkgcHMy4zLjAuMaAHqQ0&sclient=gws-wiz-serp#vhid=N6kHVs9I0BourM&vssid=mosaic" width="25" height="25">
            <p><a href="/home">Back to the main entrance</a></p>
            <p><a href="/food3">Next food photo</a></p>
        </body>
        </html>
    '''
@app.route('/food3')
def food3():
    return '''
        <html>
        <head><title>food Photo 3</title></head>
        <body>
            <h1>food Photo 3</h1>
            <p>Here's nice pet photo!</p>
            <img src="https://www.google.com/search?q=dog&sca_esv=b81c0bacdd322bb3&sca_upv=1&udm=2&biw=1846&bih=948&sxsrf=ADLYWILiEpNqrGj9JjBWJdTneJ2pdp58yA%3A1721139823599&ei=b4KWZrmbJPu1i-gPltqZqA4&ved=0ahUKEwj5jq2-4auHAxX72gIHHRZtBuUQ4dUDCBA&uact=5&oq=dog&gs_lp=Egxnd3Mtd2l6LXNlcnAiA2RvZzIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBUj4FVCXCliaFHADeACQAQCYAd8BoAH8AqoBBTAuMS4xuAEDyAEA-AEBmAIFoAK6A6gCCsICBRAAGIAEwgIHECMYJxjqAsICBBAjGCeYAwqIBgGSBwUzLjEuMaAHtAc&sclient=gws-wiz-serp#vhid=bkslsGQHvpaQaM&vssid=mosaic" width="25" height="25">
            <p><a href="/home">Back to the main entrance</a></p>
        </body>
        </html>
    '''  
@app.route('/space1')
def space1():
    return '''
        <html>
        <head><title>space Photo 1</title></head>
        <body>
            <h1>space Photo 1</h1>
            <p>Here's nice space photo!</p>
            <img src="https://stock.adobe.com/il/search?k=space&asset_id=105677222" width="25" height="25">
            <p><a href="/home">Back to the main entrance</a></p>
            <p><a href="/space2">Next space photo2</a></p>
            <p><a href="/space3">Next space photo3</a></p>

        </body>
        </html>
    '''      
@app.route('/space2')
def space2():
    return '''
        <html>
        <head><title>space Photo 2</title></head>
        <body>
            <h1>space Photo 2</h1>
            <p>Here's amazing space photo!</p>
            <img src="https://stock.adobe.com/il/search?k=space&asset_id=316550206" width="25" height="25">
            <p><a href="/home">Back to the main entrance</a></p>
            <p><a href="/space1">Next space photo1</a></p>
            <p><a href="/space3">Next space photo3</a></p>

        </body>
        </html>
    '''
@app.route('/space3')
def space3():
    return '''
        <html>
        <head><title>space Photo 3</title></head>
        <body>
            <h1>space Photo 3</h1>
            <p>Here's amazing space photo!</p>
            <img src="https://www.google.com/search?sca_esv=b81c0bacdd322bb3&sca_upv=1&sxsrf=ADLYWIJDiejEid02W02Ut6mtWiSe2fqHGA:1721139946743&q=space&udm=2&fbs=AEQNm0AVC_jJd_qrmjGRq-GYjl-cEW8osDgarSQHhl9TU0wsRQnCwzvDOZAIiHtq7ZbB1LMofR5AQT-FEZUAaBa08l1urwjga5s0JA2gNuUiZhJV_1shdVIDoic9-bawnKdKpQQTMivb8qzUTlGkhAY_bnwdJ0xohGhKAQ5UqHDLhrv-PLHKxaim_VhGrOiO71nIzY-HgCUw46d0mTtdTZsRjEPU_cdzqPlmtycbqQVgEAQ5X5-djOHMKlni4cEp-UT0I7-w1lQ2&sa=X&ved=2ahUKEwipj4n54auHAxUDh_0HHfGdCDEQtKgLegQIJxAB&biw=1846&bih=948&dpr=1#vhid=n08eidRkNCtgiM&vssid=mosaic" width="25" height="25">
            <p><a href="/home">Back to the main entrance</a></p>
            <p><a href="/space1">Next food space1</a></p>
            <p><a href="/space2">Next food space2</a></p>

        </body>
        </html>
    '''    
if __name__ == '__main__':
    app.run(debug=True)