import api from './axios';

// Fetch user data
export const getUser = async () => {
  const res = await api.get('users/');
  return res.data;
};

// Fetch user profile
export const getProfile = async () => {
  const res = await api.get('profiles/');
  return res.data;
};

// Update user profile
export const updateProfile = async (profileData) => {
  const res = await api.put('profiles/1/', profileData);  // Assuming 1 is the user's profile ID
  return res.data;
};
