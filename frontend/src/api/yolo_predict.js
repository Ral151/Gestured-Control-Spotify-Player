import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const fetchHealth = async () => {
  const res = await api.get("/health");
  return res.data;
};

export const fetchProfile = async () => {
  const res = await api.get("/spotify/profile")
  return res.data
}

export const fetchGesture = async () => {
  const res = await api.get("/gesture");
  return res.data;
};

export const fetchSpotifyCurrent = async () => {
  const res = await api.get("/spotify/current");
  return res.data;
};

export default api;