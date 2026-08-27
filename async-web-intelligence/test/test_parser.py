from src.processing.parser import parse_job_data
from src.processing.normalizer import normalize_data
from src.processing.normalizer import normalize_data

def test_parser():
    crawl_data = [
        {
            "url": "https://example.com/job",
            "markdown": """
            # Python Developer

            ABC Company

            India

            2-4 years
            """
        }
    ]

    result = parse_job_data(crawl_data)

    assert len(result) == 1

    





def test_normalization(capsys):
    data = [
        {
            "job_title": "Python Developer",
            "company": "ABC Company",
            "location": "India",
            "experience": "2-4 years",
            "job_url": "https://example.com/job"
        }
    ]

    normalize_data(data)

    captured = capsys.readouterr()

    assert "Python Developer" in captured.out
    assert "ABC Company" in captured.out
    assert "India" in captured.out
    assert "2-4 years" in captured.out
    assert "https://example.com/job" in captured.out