import axios from "axios"

import { UserLogin, Token, UserRegister } from "../schemas/auth"

const api_url = `${import.meta.env.VITE_API_URL}/security`

export async function loginUser(userData: UserLogin): Promise<string> {
    let token: string = ''
    await axios.post<Token>(
        `${api_url}/login`,
        userData,
        {headers: {'content-type': 'application/x-www-form-urlencoded'}}
    ).then(response => {
        token = response.data.access_token
    }).catch(error => {
        throw new Error(error.response.data.detail)
    })
    return token
}

export async function registerUser(userData: UserRegister): Promise<string> {
    let token: string = ''
    await axios.post<Token>(`${api_url}/register`, userData).then(response => {
        token = response.data.access_token
    }).catch(error => {
        throw new Error(error.response.data.detail)
    })
    return token
}

export function checkAuthentication(): boolean {
    if (localStorage.getItem('jwtToken')) {
        return true
    }
    return false
}
