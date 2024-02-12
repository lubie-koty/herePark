export interface UserLogin {
    username: string
    password: string
}

export interface UserRegister {
    username: string
    password: string
    first_name: string
    last_name: string
}

export interface Token {
    access_token: string
    token_type: string
}
