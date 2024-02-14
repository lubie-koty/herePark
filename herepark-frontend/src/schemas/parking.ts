export interface Position {
    lat: number
    lng: number
}

export interface ReservationInformation {
    reservation_id: number
    reservation_datetime: Date
}

export interface ParkingSpaceInformation {
    space_id: number
    position: Position
    average_rating: string
    reservations: ReservationInformation[]
}

export interface ReservationForm {
    space_id: number
    reservation_datetime: Date
}

export interface RatingForm {
    space_id: number
    rating: number
}
