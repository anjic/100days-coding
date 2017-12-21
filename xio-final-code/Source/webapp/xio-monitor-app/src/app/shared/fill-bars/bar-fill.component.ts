import {Component, Input} from '@angular/core';

@Component({
    selector: 'app-bar-fill',
    templateUrl: "./bar-fill.component.html",
    styleUrls: ["./bar-fill.component.scss"]
})
export class BarFillComponent {
    @Input() bar;
    @Input() last;

    getStyle(property, value) {
        return {[property]: value};
    }
}
