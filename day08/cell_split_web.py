from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from cell_split_lib import split_cells

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>Cell Splitting Calculator</h1>

            <form action="/calculate" method="post">
                <label>Total volume (mL):</label>
                <input type="number" step="any" name="total_volume" required>
                <br><br>

                <label>Split ratio:</label>
                <input type="number" step="any" name="split_ratio" required>
                <br><br>

                <button type="submit">Calculate</button>
            </form>
        </body>
    </html>
    """


@app.post("/calculate", response_class=HTMLResponse)
def calculate(total_volume: float = Form(...), split_ratio: float = Form(...)):
    try:
        cells, medium = split_cells(total_volume, split_ratio)

        return f"""
        <html>
            <body>
                <h1>Cell Splitting Instructions</h1>
                <p>Take {cells:.2f} mL of cells</p>
                <p>Add {medium:.2f} mL of fresh medium</p>
                <p>Final volume: {total_volume:.2f} mL</p>
                <br>
                <a href="/">Calculate again</a>
            </body>
        </html>
        """

    except ValueError as error:
        return f"""
        <html>
            <body>
                <h1>Error</h1>
                <p>{error}</p>
                <a href="/">Try again</a>
            </body>
        </html>
        """
