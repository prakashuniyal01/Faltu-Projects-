import axios from "axios";
import { getAuthToken } from "./storage.service";

const BASE_URL = "http://localhost:8080/api"

export const http = axios.create({
    baseURL: BASE_URL, // host name 
    headers: {
        'Authorization': `${getAuthToken()}`
    }
});
