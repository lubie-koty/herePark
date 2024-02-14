import axios from "axios"

import {
    ParkingSpaceInformation,
    ReservationForm,
    RatingForm
} from "../schemas/parking"

const api_url = `${import.meta.env.VITE_API_URL}/parking`

export function getParkingSpaces() {
    const token = localStorage.getItem('jwtToken')
    return axios.get<ParkingSpaceInformation[]>(
        `${api_url}/parking_spaces`,
        { headers: { Authorization: `Bearer ${token}` }}
    ).catch(error => {
        throw new Error(error.response.data.detail)
    })
}

export async function addReservation(reservationData: ReservationForm) {
    const token = localStorage.getItem('jwtToken')
    await axios.post(
        `${api_url}/reservations`,
        reservationData,
        { headers: { Authorization: `Bearer ${token}` }}
    ).catch(error => {
        throw new Error(error.response.data.detail)
    })
}

export async function addRating(ratingData: RatingForm) {
    const token = localStorage.getItem('jwtToken')
    await axios.post(
        `${api_url}/ratings`,
        ratingData,
        { headers: { Authorization: `Bearer ${token}` }}
    ).catch(error => {
        throw new Error(error.response.data.detail)
    })
}
