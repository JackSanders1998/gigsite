import { writable, derived } from 'svelte/store';

/** Store for your data. 
This assumes the data you're pulling back will be an array.
If it's going to be an object, default this to an empty object.
**/
export const apiData = writable([]);

export const gigDetails = derived(apiData, ($apiData) => {
    if ($apiData){
        console.log("in apiData");
      return $apiData.map(gig => gig);
    }
    console.log("not in apiData");
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