const baseUrl = 'http://127.0.0.1:8000'
const movieListUrl = baseUrl + '/api/movie-list/'
const titleInput = document.querySelector('#title')
const descriptionInput = document.querySelector('#description')
const imageURLInput = document.querySelector('#image-url')
const submitButton = document.querySelector('#submit')
const csrfToken = document.cookie.match(/csrftoken=(\w+);?/)[1]


async function getAllMovies(){
    const response = await fetch(movieListUrl)
    const data = await response.json()
    return data
}

async function addMovie() {
    const data = {
        title: titleInput.value,
        description: descriptionInput.value,
        image: imageURLInput.value
    }
    console.log(JSON.stringify(data))
    const response = await fetch(movieListUrl, {
        method:'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken': csrfToken,
        }
    })
    const responseData = await response.json()
    console.log(responseData)
    return responseData
}

submitButton.onclick = addMovie