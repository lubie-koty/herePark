<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { Offcanvas } from 'bootstrap'
import {
  ParkingSpaceInformation,
  ReservationForm,
  ReservationInformation,
  RatingForm
} from "../schemas/parking"
import {
  addRating,
  addReservation,
  getParkingSpaces
} from "../utils/parking"

const startDate = new Date()
const ratingOptions = [
  { id: 1, name: '⭐' },
  { id: 2, name: '⭐⭐' },
  { id: 3, name: '⭐⭐⭐' },
  { id: 4, name: '⭐⭐⭐⭐' },
  { id: 5, name: '⭐⭐⭐⭐⭐' },
]
const mapOptions = {
  zoomControl: true,
  mapTypeControl: false,
  streetViewControl: false,
  fullscreenControl: false,
  rotateControl: false
}
const center = {
  lat: Number(import.meta.env.VITE_MAP_CENTER_LAT),
  lng: Number(import.meta.env.VITE_MAP_CENTER_LNG)
}

const offcanvasBoostrap = ref(Offcanvas)

const parkingSpaces = ref<ParkingSpaceInformation[]>([])
const currentReservations = ref<ReservationInformation[]>()
const currentRating = ref<string>()
const currentSpace = ref<number>()

const selectedSpace = ref<number>()
const selectedRating = ref<number>()
const selectedDate = ref<Date>()

function showOffcanvas(space_id: number, index: number) {
  selectedSpace.value = space_id
  currentSpace.value = index
  currentReservations.value = parkingSpaces.value[index].reservations
  currentRating.value = parkingSpaces.value[index].average_rating
  offcanvasBoostrap.value.show()
}

function convertDate(date: Date) {
  const options = {
    timeZone: 'Europe/Warsaw'
  }
  const new_date = new Date(date)

  new_date.setHours(new_date.getHours() + 1)
  return new_date.toLocaleString('en-GB', options)
}

async function submitRating() {
  const data: RatingForm = {
    space_id: selectedSpace.value!,
    rating: selectedRating.value!
  }
  await addRating(data).then(() => {
    loadParkingSpaces()
    currentRating.value = parkingSpaces.value[currentSpace.value!].average_rating
  })
}

async function submitReservation() {
  const data: ReservationForm = {
    space_id: selectedSpace.value!,
    reservation_datetime: selectedDate.value!
  }
  await addReservation(data).then(() => {
    loadParkingSpaces()
    currentReservations.value = parkingSpaces.value[currentSpace.value!].reservations
  })

}

function loadParkingSpaces() {
  getParkingSpaces().then(response => {
    parkingSpaces.value = response.data
  })
}

onMounted(() => {
  offcanvasBoostrap.value = new Offcanvas(
    document.getElementById('offcanvasRight')
  )
  loadParkingSpaces()
})
</script>
<template>
<div
  class="border border-secondary-subtle mx-auto"
  style="width: fit-content"
>
  <GMapMap
    :center="center"
    :zoom="15"
    :options="mapOptions"
    map-type-id="terrain"
    style="width: 100rem; height: 50rem"
  >
    <GMapMarker
      :key="space.space_id"
      :position="space.position"
      :clickable="true"
      v-for="(space, index) in parkingSpaces"
      @click="showOffcanvas(space.space_id, index)"
    />
  </GMapMap>
</div>

<div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
  <div class="offcanvas-header" style="border-bottom: 1px solid">
      <div class="container">
        <div class="row">
          <div class="col-8">
            <h6>Parking Rating</h6>
            <div class="progress" role="progressbar" aria-label="Animated striped example" aria-valuemin="0" aria-valuemax="100">
              <div class="progress-bar progress-bar-striped progress-bar-animated" id="ratingBar"></div>
            </div>
          </div>
          <div class="col">
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#ratingCollapse" aria-expanded="false" aria-controls="ratingCollapse">
              ⭐
            </button>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
          </div>
        </div>
        <div class="row mt-2">
          <div class="collapse" id="ratingCollapse">
            <div class="card card-body">
              <select class="form-select" aria-label="selectRating" v-model="selectedRating">
                <option v-for="rating in ratingOptions" v-bind:value="rating.id">
                  {{ rating.name }}
                </option>
              </select>
              <button type="button" class="btn btn-primary mt-1" @click="submitRating">Submit</button>
            </div>
          </div>
        </div>
      </div>
  </div>
  <div class="offcanvas-body">
      <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#reservationCollapse" aria-expanded="false" aria-controls="reservationCollapse">
        Add Reservation
      </button>
      <div class="collapse mt-1" id="reservationCollapse">
        <div class="card card-body">
          <VueDatePicker
            auto-apply
            time-picker-inline
            v-model="selectedDate"
            :min-date="startDate"
            :start-date="startDate"
          />
          <button type="button" class="btn btn-primary mt-1" @click="submitReservation">Submit</button>
        </div>
      </div>
      <div class="card mt-1">
        <div class="card-body">
          <h5 class="card-title">Your Reservations</h5>
          <div style="height: 35vw">
            <ul class="list-group">
              <li
                :key="reservation.reservation_id"
                class="list-group-item"
                v-for="reservation in currentReservations"
              >
                {{ convertDate(reservation.reservation_datetime) }}
              </li>
            </ul>
          </div>
        </div>
      </div>
  </div>
</div>
</template>
<style scoped>
  #ratingBar {
    width: v-bind('currentRating')
  }
</style>
