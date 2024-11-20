from app import create_app
import webbrowser

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    webbrowser.open_new("http://127.0.0.1:5000") 