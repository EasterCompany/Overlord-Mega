let dexBtnToggle = false;

function dexDrawGui () { 
  return null;
}

function pressDexBtn () {
  if ( dexBtnToggle ) {
    dexBtnToggle = false;
  } else {
    dexBtnToggle = true;
  }
  return dexDrawGui();
}