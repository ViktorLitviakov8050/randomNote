import gkeepapi

keep = gkeepapi.Keep()
# keep.login('seevz.savage@gmail.com', 'vkshhczuhfrgwrml')
keep.login('888viktor2012@gmail.com', 'vaqiwqpuvajkjmts')
gnotes = keep.all()

for note in gnotes[:5]:
    print(note.text, note.title)
