import {Component, OnInit, OnChanges, Input} from '@angular/core';
import {IBar} from '../../ise/models/ibar.model';
import {IFillContainer} from '../../ise/models/ifillContainer.model';
import {IFillBar} from '../../ise/models/ifillbar.model';

@Component({
    selector: 'app-fill-container',
    templateUrl: './fill-container.component.html',
    styleUrls: ['./fill-container.component.scss']
})
export class FillContainerComponent implements OnInit, OnChanges {
    @Input() public container: IFillContainer;
    @Input() public scaleContainers: number[];
    @Input() public scaleContainerSize: number;
    @Input() public first: boolean;
    public fillBars: IFillBar[];
    public ovalFill: string;
    public color: string;

    getStyle(property: string, value: any) {
        return {[property]: value};
    }

    setFillBars(bars: IBar[]) {
        return bars.map((bar, index) => {
            let fillColor = bar.color;
            let ovalFill = {
                R: fillColor.R + 30,
                G: fillColor.G + 30,
                B: fillColor.B + 30
            };
            let offset = bars.slice(0, index).reduce((sum, curr) => {
                return sum + ((curr.data.value / this.container.storageSize) * 100);
            }, 0);

            return {
                data: bar.data,
                offset: `${offset}%`,
                width: ((bar.data.value / this.container.storageSize) * 100).toFixed(1),
                fillColor: bar.gradient,
                ovalFill: `rgb(${ovalFill.R}, ${ovalFill.G}, ${ovalFill.B})`
            };
        });
    }

    ngOnInit() {
        this.ovalFill = `rgb(${this.container.color.R + 50}, ${this.container.color.G + 50}, ${this.container.color.B + 50})`;
        this.color = `rgba(${this.container.color.R}, ${this.container.color.G}, ${this.container.color.B}, 0.5)`;
    }

    ngOnChanges() {
        this.fillBars = this.setFillBars(this.container.bars);
    }
}
