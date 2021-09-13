import { writable, derived } from 'svelte/store';


// Handle Gig Data
export const apiData = writable();

export const gigDetails = derived(apiData, ($apiData) => {
    if ($apiData){
        console.log("in apiData");
        return $apiData.map(gig => gig);
    }
    console.log("not in apiData");
    return [];
  });

// Handle User Data
export const userData = writable();

export const userDetails = derived(userData, ($userData) => {
    if ($userData){
        console.log("in userData");
        return $userData.map(user => user);
    }
    console.log("not in userData");
    return [];
  });

export const isAuthenticated = writable(false);
export const user = writable({});
export const popupOpen = writable(false);
export const error = writable();

export const gigs = writable([]);

export const user_gigs = derived([gigs, user], ([$gigs, $user]) => {
  let logged_in_user_gigs = [];

  if ($user && $user.email) {
    logged_in_user_gigs = $gigs.filter((gig) => gig.user === $user.email);
  }

  return logged_in_user_gigs;
});