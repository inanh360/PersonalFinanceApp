import { useState, useEffect } from 'react';
import { getProfile, updateProfile } from '../api/user';

export default function Profile() {
  const [profile, setProfile] = useState({});
  const [bio, setBio] = useState('');
  const [avatar, setAvatar] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      const data = await getProfile();
      setProfile(data);
      setBio(data.bio || '');
    };

    fetchProfile();
  }, []);

  const handleUpdateProfile = async (e) => {
    e.preventDefault();

    const updatedData = {
      bio,
      avatar,
    };

    const data = await updateProfile(updatedData);
    setProfile(data);  // Update state after successful profile update
  };

  return (
    <div>
      <h2>{profile.user?.username}'s Profile</h2>
      <img src={profile.avatar} alt="Avatar" />
      <form onSubmit={handleUpdateProfile}>
        <div>
          <label>Bio</label>
          <textarea 
            value={bio} 
            onChange={(e) => setBio(e.target.value)} 
            placeholder="Write a short bio..." 
          />
        </div>
        <div>
          <label>Avatar</label>
          <input 
            type="file" 
            onChange={(e) => setAvatar(e.target.files[0])} 
          />
        </div>
        <button type="submit">Update Profile</button>
      </form>
    </div>
  );
}
