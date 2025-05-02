from matchman import create_app

app = create_app()


def main():
    app.run(host="0.0.0.0", port=3000, debug=True)


if __name__ == "__main__":
    main()
