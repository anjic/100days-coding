import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseComponent } from './ise.component';

describe('IseComponent', () => {
  let component: IseComponent;
  let fixture: ComponentFixture<IseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
