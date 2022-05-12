window.onload = function () {
    apiGet('/api/universities')
        .then(data => {
            console.log(data)
            let uniTable = document.getElementById('uni-list')
            console.log(uniTable)
            for (uni of data) {
                let listRow = document.createElement('li')
                listRow.addEventListener('click', function () {
                    window.open(`https://google.com/search?q=${uni.university}`)
                })
                listRow.addEventListener('mouseover', function () {
                    listRow.classList.add('text-color-red')
                })
                listRow.addEventListener('mouseleave', function (){
                    listRow.classList.remove('text-color-red')
                })
                listRow.innerText = uni.university
                uniTable.appendChild(listRow)
            }
        })
}


let regButton = document.getElementById('bt_register')
regButton.addEventListener('click', function () {
    let name = document.getElementById('name').value
    let email = document.getElementById('email').value
    let uni = document.getElementById('uni').value
    let course = document.getElementById('course').value
    let startingDate = document.getElementById('starting-date').value
    let password = document.getElementById('password').value
    apiPost('/api/registration', {
        'name': name,
        'email': email,
        'uni': uni,
        'course': course,
        'starting_date': startingDate,
        'password': password
    })
        .then(data => {
            console.log(data)
        })
})

async function apiPost(url, data) {
    const response = await fetch(url, {
        method: 'POST', headers: {
            'Content-Type': 'application/json'
        }, body: JSON.stringify(data)
    })
    if (response.ok) {
        return response.json()
    }
}

async function apiGet(url) {
    const response = await fetch(url, {method: 'GET'})
    if (response.ok) {
        return response.json()
    }
}


