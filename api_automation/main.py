import unittest
import pytest

if __name__ == "__main__":
    #pytest.main(["--html=1.html --css=report.css"])
    pytest.main(["--html=report.html", "--self-contained-html", "--css=report.css"])

