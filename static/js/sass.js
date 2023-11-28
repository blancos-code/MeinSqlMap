import { MDCDataTable } from "@material/data-table";
import { MDCRipple } from "@material/ripple";

const iconButtonRipple = new MDCRipple(
  document.querySelector(".mdc-icon-button")
);
iconButtonRipple.unbounded = true;
const dataTable = new MDCDataTable(document.querySelector(".mdc-data-table"));
