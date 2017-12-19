import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseListComponent } from './ise-list.component';

describe('IseListComponent', () => {
  let component: IseListComponent;
  let fixture: ComponentFixture<IseListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
