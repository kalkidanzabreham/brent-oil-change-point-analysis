const BASE_URL = "http://localhost:5000/api";

export const fetchPrices = async () => {
  const res = await fetch(`${BASE_URL}/prices`);
  return res.json();
};

export const fetchEvents = async () => {
  const res = await fetch(`${BASE_URL}/events`);
  return res.json();
};

export const fetchChangePoints = async () => {
  const res = await fetch(`${BASE_URL}/changepoints`);
  return res.json();
};
