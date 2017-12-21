import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseInfoCardComponent } from './ise-info-card.component';

describe('IseInfoCardComponent', () => {
  let component: IseInfoCardComponent;
  let fixture: ComponentFixture<IseInfoCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseInfoCardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseInfoCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
