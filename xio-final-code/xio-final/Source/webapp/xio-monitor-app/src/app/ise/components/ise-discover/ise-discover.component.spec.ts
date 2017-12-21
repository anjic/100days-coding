import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseDiscoverComponent } from './ise-discover.component';

describe('IseDiscoverComponent', () => {
  let component: IseDiscoverComponent;
  let fixture: ComponentFixture<IseDiscoverComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseDiscoverComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseDiscoverComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
