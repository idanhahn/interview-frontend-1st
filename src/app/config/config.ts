/**
 * Created by idanhahn on 11/11/2016.
 */

interface AuthConfiguration {
  clientID: string;
  domain: string;
}

const authConfig_platform: AuthConfiguration = {

  // waycare-platform
  clientID: 'aXXGyeA275CQ5nD51Q6hyCikKNI24FUG',
  domain: 'waycare-general.auth0.com',
};


const authConfig_channel10: AuthConfiguration = {

  // waycare-platform
  clientID: 'SOjrSlFe7xOYs7BnIrJFsUuDmJTbzLFV',
  domain: 'waycare-general.auth0.com',
};


const authConfig_platform_testing: AuthConfiguration = {

  // waycare-platform - fbtest
  clientID: 'CmonXbrtw1grdJFddXh636y4HlUj4hrw',
  domain: 'waycare-general.auth0.com',
};


const firebaseConfig_main = {
  apiKey: 'AIzaSyBQ7eTEoK1v1IzYhXmQaD6POFH9crf5X18',
  authDomain: 'waycare-db.firebaseapp.com',
  databaseURL: 'https://waycare-db.firebaseio.com',
  storageBucket: 'waycare-db.appspot.com',
  messagingSenderId: '1032655196539'
};

export const fireBaseConfig_m_demo = {
  apiKey: 'AIzaSyCVnkWsJa-DwvaHDKPbNwhe4P96mEmJ5Yc',
  authDomain: 'm-demo-238f6.firebaseapp.com',
  databaseURL: 'https://m-demo-238f6.firebaseio.com',
  projectId: 'm-demo-238f6',
  storageBucket: 'm-demo-238f6.appspot.com',
  messagingSenderId: '118618701734'
};


// dev - one DB for all sites
const firebaseConfig_dev = {

  // dev-test
  apiKey: 'AIzaSyB0ePipSA6oPpyoSKQShOKIpWwB4a2BPfY',
  authDomain: 'platformdev1-e40d7.firebaseapp.com',
  databaseURL: 'https://platformdev1-e40d7.firebaseio.com',
  storageBucket: 'platformdev1-e40d7.appspot.com',
  messagingSenderId: '258875038188'
};
//export const firebaseConfig = firebaseConfig_main; // =====>>> Select here <======

export const firebaseConfig = fireBaseConfig_m_demo; // =====>>> Select here <======


// TODO: do we use it?
export const googleConfig = {
  apiKey: 'AIzaSyAtQtj9eP0ma3wQk0qAFZ8xsDZKzwHvKd0',
  authDomain: 'rapid-spider-123610.firebaseapp.com',
  databaseURL: 'https://rapid-spider-123610.firebaseio.com',
  storageBucket: 'rapid-spider-123610.appspot.com',
  messagingSenderId: '93401083074'
};


// Additional configuration here


export const appDefaults = {
  defaultSite: 'lv',
  startType: 'Incident',
  numEntriesToDisplay: 5,
};


export const config = {};


// Per site information

export const siteConfig = {

  ayalon: {
    mapConfig: {
      center: {
        lat: 32.088837,
        lng: 34.861565
      },
      zoom: 13,
    },
    sliderConfig: {
      min: 8,
      max: 18,
      step: 2
    },
    authConfig: authConfig_platform,
    dDay: '2016-09-27'
  },


  fll: {
    mapConfig: {
      center: {
        lat: 26.120451,
        lng: -80.068923
      },
      zoom: 13,
    },
    sliderConfig: {
      min: 0,
      max: 22,
      step: 2
    },
    authConfig: authConfig_platform,
    dDay: '2016-09-27'
  },

  lv: {
    mapConfig: {
      center: {
        lat: 36.138954,
        lng: -114.994764
      },
      zoom: 13,
    },
    sliderConfig: {
      min: 0,
      max: 22,
      step: 2
    },
    authConfig: authConfig_platform,
    dDay: '2017-04-2'
  },

  tampa: {
    mapConfig: {
      center: {
        lat: 27.983834,
        lng: -82.409328
      },
      zoom: 15,
    },
    sliderConfig: {
      min: 0,
      max: 22,
      step: 2
    },
    authConfig: authConfig_platform,
    dDay: '2016-09-27'
  },


};

