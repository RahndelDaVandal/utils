from pathlib import Path
from flask import Flask,send_from_directory

app = Flask(__name__)

FILES_DIR = Path.cwd()

@app.route('/get/<path:path>',methods = ['GET','POST'])
def get_files(path):

    """Download a file."""
    try:
        return send_from_directory(
          FILES_DIR, 
          path, 
          as_attachment=True
          )
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
  print(f'Serving: {FILES_DIR}\n')
  app.run(
    use_reloader=False, 
    debug=True
    )
