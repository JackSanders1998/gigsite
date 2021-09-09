import { writable, derived } from 'svelte/store';

/** Store for your data. 
This assumes the data you're pulling back will be an array.
If it's going to be an object, default this to an empty object.
**/
export const apiData = writable([]);

/** Data transformation.
**/
export const gigDetails = derived(apiData, ($apiData) => {
    if ($apiData){
        console.log("in apiData");
      return $apiData.map(gig => gig);
    }
    console.log("not in apiData");
    return [];
  });