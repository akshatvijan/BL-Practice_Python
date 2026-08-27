def parse_job_data(crawl_data):
    parsed_results = []

    for crawl in crawl_data:
        markdown = crawl["markdown"]

        job_title = None
        company = None
        location = None
        experience = None

        lines = markdown.splitlines()

        for i in range(len(lines)):
            line = lines[i].strip()

            if not job_title:
                if "# " in line:
                    job_title = line[len("# "):].strip()
                elif "## " in line:
                    job_title = line[len("## "):].strip()

            if job_title and not location:
                if i > 0 and lines[i - 1].strip() == job_title:
                    location = line

            if "Minimum Qualifications:" in line:
                experience = lines[i + 1].strip()[2:]

            elif "Required Skills And Experience" in line:
                experience = lines[i + 1].strip()[2:]

            elif line == "## Qualifications":
                experience = lines[i + 1].strip()[2:]

            if "Entrata logo" in line:
                company = "Entrata"

            elif "SmartRecruiters Inc logo" in line:
                company = "SmartRecruiters Inc"

            elif "SingleStore Logo" in line:
                company = "SingleStore"

        parsed_results.append({
            "job_title": job_title,
            "company": company,
            "location": location,
            "experience": experience,
            "job_url": crawl["url"]
        })

    return parsed_results