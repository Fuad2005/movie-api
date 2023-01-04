
const iaxios = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/'

})

async function showMovieList(){
    const response = await iaxios.get('movie-list/')
    console.log(response)
}



async function createMovie(data) {
    const response = await iaxios.post('movie-list/', data)
    console.log(response)
}


async function showMovie(id) {
    const response = await iaxios.get('movie-list/' + id + '/')
    console.log(response)
}


async function deleteMovie(id) {
    const response = await iaxios.delete('movie-list/' + id + '/')
    console.log(response)
}



async function updateMovie(id, data) {
    const response = await iaxios.put('movie-list/' + id + '/', data)
}