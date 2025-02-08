

    function fetchRankedResumes() {
        fetch('/ranked_resumes')
        .then(response => response.json())
        .then(data => {
            let list = document.getElementById('resumeList');
            list.innerHTML = '';
            data.forEach(resume => {
                let item = document.createElement('li');
                item.textContent = ${resume.name} - Score: ${resume.score};
                list.appendChild(item);
            });
        });
    }
