import axios from 'axios';
import { toast } from 'react-toastify';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
  withCredentials: true,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

const handleError = (error) => {
  let errorMessage = 'An error occurred, please try again later.';
  if (error.response) {
    errorMessage = error.response.data.message || error.response.data.errors?.password?.[0] || 'Something went wrong.';
    if (error.response.status === 401) {
      localStorage.removeItem('access_token');
      localStorage.removeItem('user');
    }
  } else if (error.request) {
    errorMessage = 'Server not responding.';
  } else {
    errorMessage = error.message;
  }
  throw new Error(errorMessage);
};

// --- AUTH APIs ---
export const loginUser = async (credentials) => {
  try {
    const { data } = await api.post('/auth/login/', credentials);
    if (data.success) {
      localStorage.setItem('access_token', data.token);
      localStorage.setItem('user', JSON.stringify(data.user));
      toast.success(data.message);
      const modalEl = document.getElementById('accountModal');
      const modal = window.bootstrap.Modal.getInstance(modalEl);
      if (modal) modal.hide();
    }
    return data;
  } catch (error) {
    toast.error(handleError(error));
    throw error;
  }
};

export const registerUser = async (userData) => {
  try {
    const { data } = await api.post('/auth/register/', userData);
    if (data.success) {
      localStorage.setItem('access_token', data.token);
      localStorage.setItem('user', JSON.stringify(data.user));
      toast.success(data.message);
      const modalEl = document.getElementById('accountModal');
      const modal = window.bootstrap.Modal.getInstance(modalEl);
      if (modal) modal.hide();
    }
    return data;
  } catch (error) {
    toast.error(handleError(error));
    throw error;
  }
};

export const logoutUser = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('user');
  toast.success('Logged out successfully');
  window.location.href = '/';
};

// --- DATA APIs ---
export const fetchSiteSettings = async () => {
  try {
    const { data } = await api.get('/settings/');
    return data.data || {};
  } catch (error) { throw new Error(handleError(error)); }
};

export const fetchBanners = async () => {
  try {
    const { data } = await api.get('/banners/');
    return data.data || [];
  } catch (error) { throw new Error(handleError(error)); }
};

export const fetchCategories = async () => {
  try {
    const { data } = await api.get('/categories/');
    return data.data || [];
  } catch (error) { throw new Error(handleError(error)); }
};

export const fetchBrands = async () => {
  try {
    const { data } = await api.get('/brands/');
    return data.data || [];
  } catch (error) { throw new Error(handleError(error)); }
};

export const fetchFeaturedProducts = async (limit = 8) => {
  try {
    const { data } = await api.get(`/products/featured/?limit=${limit}`);
    return data.data || [];
  } catch (error) { throw new Error(handleError(error)); }
};

export const fetchFlashSaleProducts = async () => {
  try {
    const { data } = await api.get('/products/flash-sale/');
    return data.data || [];
  } catch (error) { throw new Error(handleError(error)); }
};

export const fetchReviews = async () => {
  try {
    const { data } = await api.get('/reviews/');
    return data.data || [];
  } catch (error) { throw new Error(handleError(error)); }
};

export const fetchBlogs = async () => {
  try {
    const { data } = await api.get('/blogs/');
    return data.data || [];
  } catch (error) { throw new Error(handleError(error)); }
};

export const fetchProductDetails = async (slug) => {
  try {
    const { data } = await api.get(`/products/${slug}/`);
    return data.data;
  } catch (error) { throw new Error(handleError(error)); }
};

export const addToCart = async (payload) => {
  try {
    const { data } = await api.post('/cart/add/', payload);
    toast.success(data.message || 'Added to cart');
    return data;
  } catch (error) {
    toast.error(handleError(error));
    throw error;
  }
};

export default api;