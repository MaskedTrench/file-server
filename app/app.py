from fastapi import FastAPI, File, UploadFile


app = FastAPI( debug= True )


@app.get('/')
async def get_all_docs():
    return []


@app.get('/status')
async def get_status():
    return []


@app.post('/file')
async def post_file(file: UploadFile):
    return { 'file_name': file.filename }
